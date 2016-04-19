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

            int x = int.Parse(line);

            if (x % 2 == 0)
                Console.WriteLine("1");
            else
                Console.WriteLine("0");
        }
    }
}
