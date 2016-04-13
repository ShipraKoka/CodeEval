using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace Multiply_Lists
{
    class Program
    {
        static void Main(string[] args)
        {
            using (StreamReader reader = File.OpenText(args[0]))
                while (!reader.EndOfStream)
                {
                    // reads each line
                    string line = reader.ReadLine().Trim();
                    if (null == line)
                        continue;

                    List<String> numbers = new List<String>();
                    numbers = line.Split('|').ToList();

                    List<String> newNumbers = new List<String>();
                    foreach (string number in numbers)
                    {
                        string x = number.Trim();
                        newNumbers.Add(x);

                    }

                    List<String> valueSetOne = new List<String>();
                    List<String> valueSetTwo = new List<String>();

                    valueSetOne = newNumbers[0].Split(' ').ToList();
                    valueSetTwo = newNumbers[1].Split(' ').ToList();


                    int i = 0;
                    List<String> results = new List<String>();
                    foreach (string value in valueSetOne)
                    {
                        int num1 = int.Parse(value);
                        string product = (multiply(num1, i, valueSetTwo)).ToString();
                        results.Add(product);
                        i++;
                    }

                    StringBuilder result = new StringBuilder();
                    foreach (string s in results)
                    {
                        result.Append(s + " ");
                    }

                    Console.WriteLine(result.ToString());
                    Console.WriteLine();

                }
        }

        static int multiply(int x, int i, List<String> set)
        {
            int num2 = int.Parse(set[i]);
            int product = x * num2;
            return product;
        }
    }
}
