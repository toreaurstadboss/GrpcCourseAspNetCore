using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Google.Protobuf.WellKnownTypes;
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
        private MeterReadingService.MeterReadingServiceClient _client;

        public Worker(ILogger<Worker> logger, IConfiguration configuration, ReadingFactory factory)
        {
            _logger = logger;
            _configuration = configuration;
            _factory = factory;
        }

        protected MeterReadingService.MeterReadingServiceClient Client
        {
            get
            {
                if (_client == null)
                {
                    var channel = GrpcChannel.ForAddress(_configuration.GetValue<string>("Service:ServerUrl"));
                    _client = new MeterReadingService.MeterReadingServiceClient(channel);
                    
                }

                return _client;

            }
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);

                var customerId = _configuration.GetValue<int>("Service:CustomerId");

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
                var result = await Client.AddReadingAsync(pkt);

                if (result.Successful == ReadingStatus.Success)
                {
                    _logger.LogInformation("Successfully sent");
                }
                else
                {
                    _logger.LogInformation("Failed to send");
                }

                await Task.Delay(_configuration.GetValue<int>("Service:DelayInterval"), stoppingToken);
            }
        }
    }
}
