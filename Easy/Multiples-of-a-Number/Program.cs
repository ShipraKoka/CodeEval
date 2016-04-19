using System;
using System.Collections.Generic;
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
                int x = int.Parse(numbers[0]);
                int n = int.Parse(numbers[1].TrimStart());
				
                int result = 0;
                int i = 1;
				
                while (result < x)
                {
                    result = n * i;
                    i++;
                }
				
                Console.WriteLine(result.ToString());
            }
        
    }

}
