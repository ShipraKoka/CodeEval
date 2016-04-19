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

			string digits = line.Trim().Replace("\n", " ");

			int sum = 0;
			foreach (var d in digits)
			{
				sum += (int)Char.GetNumericValue(d);
			}
			
			Console.WriteLine(sum);
		}
    }
}
