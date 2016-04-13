using System;
using System.Text;
using System.IO;

class Program
{
	static void Main(string[] args)
	{
		using (StreamReader reader = File.OpenText(args[0]))
		while (!reader.EndOfStream)
		{
			// reads each line
			string line = reader.ReadLine();
			if (null == line)
				continue;
			string newLine = (swapCase(line));
			Console.WriteLine(newLine);
		}
	}

	static string swapCase(string x)
	{
		StringBuilder xLine = new StringBuilder();
		for (int i = 0; i < x.Length; i++)
		{
			if (char.IsLetter(x[i]) && char.IsUpper(x[i]))
				xLine.Append(char.ToLower(x[i]));
			else if (char.IsLetter(x[i]) && char.IsLower(x[i]))
				xLine.Append(char.ToUpper(x[i]));
			else
				xLine.Append(x[i]);
		}
		return xLine.ToString();
	}
}
