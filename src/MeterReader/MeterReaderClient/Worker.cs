using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Security.Cryptography.X509Certificates;
using System.Threading;
using System.Threading.Tasks;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using MeterReaderWeb.Services;
using Microsoft.Extensions.Configuration;

namespace MeterReaderClient
{
    public class Worker : BackgroundService
    {
        private readonly ILogger<Worker> _logger;
        private readonly IConfiguration _configuration;
        private readonly ReadingFactory _factory;
        private readonly ILoggerFactory _loggerFactory;
        private MeterReadingService.MeterReadingServiceClient _client;
        private string _token;
        private DateTime _expiration = DateTime.MinValue;

        public Worker(ILogger<Worker> logger, IConfiguration configuration, ReadingFactory factory, ILoggerFactory loggerFactory)
        {
            _logger = logger;
            _configuration = configuration;
            _factory = factory;
            _loggerFactory = loggerFactory;
        }

        protected MeterReadingService.MeterReadingServiceClient Client
        {
            get
            {
                if (_client == null)
                {
                    var cert = new X509Certificate2(_configuration["Service:CertFileName"], _configuration["Service:CertPassword"]);

                    var handler = new HttpClientHandler();
                    handler.ClientCertificates.Add(cert);

                    var client = new HttpClient(handler);

                    var opt = new GrpcChannelOptions
                    {
                        HttpClient = client,
                        LoggerFactory = _loggerFactory
                    };

                    var channel = GrpcChannel.ForAddress(_configuration.GetValue<string>("Service:ServerUrl"), opt);
                    _client = new MeterReadingService.MeterReadingServiceClient(channel);
                    
                }

                return _client;

            }
        }

        protected bool NeedsLogin() => string.IsNullOrWhiteSpace(_token) || _expiration > DateTime.UtcNow;

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            var counter = 0;
            var customerId = _configuration.GetValue<int>("Service:CustomerId");


            while (!stoppingToken.IsCancellationRequested)
            {
                counter++;

                //if (counter % 10 == 0)
                //{
                //    Console.WriteLine("Sending Diagnostics");
                //    var stream = Client.SendDiagnostics();
                //    for (int i = 0; i < 5; i++)
                //    {
                //        var readingRes = await _factory.Generate(customerId);
                //        await stream.RequestStream.WriteAsync(readingRes);
                //    }

                //    await stream.RequestStream.CompleteAsync();
                //}

                _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);


                var pkt = new ReadingPacket()
                {
                    Successful = ReadingStatus.Success,
                    Notes = "This is our test"
                };

                var reading = new ReadingMessage();
                reading.CustomerId = customerId;
                reading.ReadingValue = 10000;
                reading.ReadingTime = Timestamp.FromDateTime(DateTime.UtcNow);

                for (int i = 0; i < 5; i++)
                {
                    pkt.Readings.Add(await _factory.Generate(customerId));
                }

                try
                {
                    //if (!NeedsLogin() || await GenerateToken())
                    //{
                    //    var headers = new Metadata();
                    //    headers.Add("Authorization", $"Bearer {_token}");

                    var result = await Client.AddReadingAsync(pkt); // headers: headers);

                        if (result.Successful == ReadingStatus.Success)
                        {
                            _logger.LogInformation("Successfully sent");
                        }
                        else
                        {
                            _logger.LogInformation("Failed to send");
                        }
                    //}
                }
                catch (RpcException ex)
                {
                    if (ex.StatusCode == StatusCode.OutOfRange)
                    {
                        _logger.LogError($"{ex.Trailers}");
                    }
                    _logger.LogError($"Exception Thrown: {ex}");
                }

                await Task.Delay(_configuration.GetValue<int>("Service:DelayInterval"), stoppingToken);
            }
        }

        private async Task<bool> GenerateToken()
        {
            var request = new TokenRequest
            {
                Username = _configuration["Service:Username"],
                Password = _configuration["Service:Password"]
            };
            var response = await Client.CreateTokenAsync(request);
            if (response.Success)
            {
                _token = response.Token;
                _expiration = response.Expiration.ToDateTime();

                return true;
            }

            return false;
        }
    }
}
