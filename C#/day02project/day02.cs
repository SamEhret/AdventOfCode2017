using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace day02project
{
    public class Day02
    {
        public void Run()
        {
            List<string> input = new List<string>();
            using (var streamReader = new StreamReader("day02input.txt", Encoding.Default))
            {
                while (!streamReader.EndOfStream)
                {
                    input.Add(Regex.Replace(streamReader.ReadLine(), @"\s+", " "));
                }
            }

            Part01(input);
            Part02(input);
        }

        private void Part01(List<string> input)
        {
            var sum = 0;

            for (int i = 0; i < input.Count; i++)
            {
                var tempList = input[i].Split().Select(Int32.Parse).ToList();
                tempList.Sort();

                sum += (tempList[tempList.Count - 1] - tempList[0]);
            }
            Console.WriteLine("Part 1 Answer: " + sum);
        }

        private void Part02(List<string> input)
        {
            var sum = 0;

            for (int i = 0; i < input.Count; i++)
            {
                var tempList = input[i].Split().Select(Int32.Parse).ToList();

                for (int x = 0; x < tempList.Count; x++)
                {
                    for (int y = x + 1; y < tempList.Count; y++)
                    {
                        if (tempList[x] % tempList[y] == 0)
                        {
                            sum += (tempList[x] / tempList[y]);
                        }
                        else if (tempList[y] % tempList[x] == 0)
                        {
                            sum += (tempList[y] / tempList[x]);
                        }
                    }
                }
            }
            Console.WriteLine("Part 2 Answer: " + sum);
        }
    }
}
