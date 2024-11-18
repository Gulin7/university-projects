using System.Collections.Generic;
using System.Threading.Tasks;
using Lab4.Socket;

namespace Lab4.Parser
{
    internal class TaskSolution : Common
    {
        protected override string ParserType => "Task";

        public TaskSolution(List<string> urls) : base(urls)
        {
        }

        protected override async void Run()
        {
            var tasks = Map(async (index, url) => await Start(SocketHandler.Create(url, index)));
            await Task.WhenAll(tasks);
        }


        private Task Start(SocketHandler socket)
        {
            socket.BeginConnectAsync().Wait();
            LogConnected(socket);

            var sendTask = socket.BeginSendAsync();
            sendTask.Wait();
            var numberOfSentBytes = sendTask.Result;
            LogSent(socket, numberOfSentBytes);

            socket.BeginReceiveAsync().Wait();
            LogReceived(socket);

            socket.ShutdownAndClose();
            return Task.CompletedTask;
        }
    }
}