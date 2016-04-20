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
                line = line.Trim();
                if (line.Length <= 55)
                    Console.WriteLine(line);
                else
                {
                    string s1 = line.Substring(0, 40); 
                    int i = s1.Length - 1;
                    char last = s1[i];
                    
                    if (Char.IsLetterOrDigit(last))
                        {
                        while (Char.IsLetterOrDigit(s1[i]) && i > 0){
                            i--;
                        }

                        if (i == 0)
                        {
                            Console.WriteLine("{0}... <Read More>", s1.TrimEnd());
                        }
                        else
                        {
                            s1 = s1.Substring(0, i);
                            Console.WriteLine("{0}... <Read More>", s1.TrimEnd());
                        }
                        }
                    else
                    {
                        Console.WriteLine("{0}... <Read More>", s1.TrimEnd());
                    }
                   
                }
        }

    }
}
