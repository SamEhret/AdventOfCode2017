using System;
using System.Collections.Generic;

namespace day03project
{
    public class Day03
    {
        public void Run()
        {
            int target = 368078;
            Part01(target, out int x, out int y);
            int distance = (Math.Abs(x) + Math.Abs(y));
            Console.WriteLine("Part 1 Answer: " + distance);

            int part02answer = Part02(target);
            Console.WriteLine("Part 2 Answer: " + part02answer);

        }

        private void Part01(int target, out int x, out int y)
        {
            int i = 1;
            x = 0;
            y = 0;

            int xMax = 0;
            int xMin = 0;
            int yMax = 0;
            int yMin = 0;

            while (true)
            {
                //Right
                while (x <= xMax)
                {
                    x++;
                    if (++i == target) return;
                }
                xMax = x;
                    
                //Up
                while (y <= yMax)
                {
                    y++;
                    if (++i == target) return;
                }
                yMax = y;

                //Left
                while (x >= xMin)
                {
                    x--;
                    if (++i == target) return;
                }
                xMin = x;

                //Down
                while (y >= yMin)
                {
                    y--;
                    if (++i == target) return;
                }
                yMin = y;
            }
        }

        private int Part02(int target)
        {
            int x = 0;
            int y = 0;

            int xMax = 0;
            int xMin = 0;
            int yMax = 0;
            int yMin = 0;

            Dictionary<int, Dictionary<int, int>> values = new Dictionary<int, Dictionary<int, int>>();

            addValue(0, 0, 1, values);

            while (true)
            {
                //Right
                while (x <= xMax)
                {
                    x++;
                    calculateValue(x, y, values);
                    if (values[x][y] > target) return values[x][y];
                }
                xMax = x;

                //Up
                while (y <= yMax)
                {
                    y++;
                    calculateValue(x, y, values);
                    if (values[x][y] > target) return values[x][y];
                }
                yMax = y;

                //Left
                while (x >= xMin)
                {
                    x--;
                    calculateValue(x, y, values);
                    if (values[x][y] > target) return values[x][y];
                }
                xMin = x;

                //Down
                while (y >= yMin)
                {
                    y--;
                    calculateValue(x, y, values);
                    if (values[x][y] > target) return values[x][y];
                }
                yMin = y;
            }
        }

        private void calculateValue(int x, int y, Dictionary<int, Dictionary<int, int>> values)
        {
            var total = 0;

            for (int a = x - 1; a <= x + 1; a++)
            {
                for (int b = y - 1; b <= y + 1; b++)
                {
                    if ((!(a == x && b == y)) && values.ContainsKey(a) && values[a].ContainsKey(b))
                    {
                        total += values[a][b];
                    }
                }
            }
            addValue(x, y, total, values);
        }

        private void addValue(int x, int y, int value, Dictionary<int, Dictionary<int, int>> values)
        {
            if (!values.ContainsKey(x))
            {
                values.Add(x, new Dictionary<int, int>());
            }
            values[x][y] = value;
        }
    }
}
