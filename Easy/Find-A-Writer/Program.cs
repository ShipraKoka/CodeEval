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

                string writer = "";
                string[] writers = line.Split('|');
                string letters = writers[0];
                string numbers = writers[1].TrimStart();
                string[] key = numbers.Split(' ');

                foreach (string item in key)
                {
                    writer += letters[int.Parse(item) - 1];
                }

                Console.WriteLine(writer);
        }
    }
}
