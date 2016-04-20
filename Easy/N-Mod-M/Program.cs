using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;

                string[] numbers = line.Split(',');
                int N = int.Parse(numbers[0]);
                int M = int.Parse(numbers[1]);

                int quotient = N / M;
                int remainder = N - (quotient * M);
                Console.WriteLine(remainder);
        }
    }
}
