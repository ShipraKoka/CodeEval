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

                string[] temp = line.Split(',');
                string phrase = temp[0];
                char t = char.Parse(temp[1]);

                int pos = 0;
                for (int i = 0; i < phrase.Length; i++)
                {
                    if (t == phrase[i])
                        pos = i;
                }
                
                if (pos != 0)
                    Console.WriteLine(pos);
                else
                    Console.WriteLine("-1");
        }
    }
}
