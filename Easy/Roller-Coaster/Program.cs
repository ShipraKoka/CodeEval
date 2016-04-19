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

                string sentence = line.Replace("\n", " ");
                List<char> words = new List<char>();
                foreach (char s in sentence)
                {
                    words.Add(s);
                }

                int index;
                for (int i = 0; i < words.Count; i++)
                {
                    index = i;
                    // Check if 1st character
                    if (i == 0)
                        continue;

                    // Check if not a letter
                    if (!Char.IsLetter(words[i]))
                        continue;

                    // If letter, check if previous character is a lowercase letter
                    else if (Char.IsLower(words[i - 1]))
                        words[i] = Char.ToUpper(words[i]);

                    // If letter, check if previous character is not a letter
                    else if (!Char.IsLetter(words[i - 1]))
                    {
                        // Check each previous character until the 1st one that is a letter
                        while (!Char.IsLetter(words[index - 1]))
                        {
                            index--;
                        }

                        // Once letter is reached, check if lowercase
                        if (Char.IsLower(words[index - 1]))
                            words[i] = Char.ToUpper(words[i]);
                    }
                    else
                        continue;  
                }

                string newSentence = string.Join("", words.ToArray());
                Console.WriteLine(newSentence);
            }
    }

}
