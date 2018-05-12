using System;
using System.Collections.Generic;
using System.IO;

namespace day05project
{
    public static class Day05
    {
        public static void Run()
        {
            var line = "";
            var input = new List<int>();
            var file = new StreamReader(@"day05input.txt");
            while((line = file.ReadLine()) != null)  
            {  
                input.Add(int.Parse(line));
            }

            Part01(new List<int>(input));
            Part02(new List<int>(input));
        }

        private static void Part01(IList<int> input)
        {
            var i = 0;
            var count = 0;
            
            while (i >= 0 && i < input.Count)
            {
                var increment = input[i];
                
                input[i] += 1;
                i = i + increment;
                count += 1;
            }
            Console.WriteLine($"Part 1 Answer: {count}");
        }

        private static void Part02(IList<int> input)
        {
            var i = 0;
            var count = 0;

            while (i >= 0 && i < input.Count)
            {
                var increment = input[i];

                if (increment >= 3)
                {
                    input[i] -= 1;
                }
                else
                {
                    input[i] += 1;
                }
                i += increment;
                count += 1;
            }
            Console.WriteLine($"Part 2 Answer: {count}");
        }
    }
}