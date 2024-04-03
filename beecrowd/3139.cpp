#include <iostream>
#include <math.h>
#include <queue>

using namespace std;

int main()
{
  long long cur, goal, num, average = 0, days = 0, sum = 0;
  queue<long long> followers;

  cin >> cur >> goal;

  for (int i = 0; i < 30; i++)
  {
    cin >> num;
    sum += num;
    followers.push(num);
  }

  while(cur < goal){
    average = ceil(sum / 30.0);

    cur += average;
    days++;
    sum = sum - followers.front() + average;

    followers.pop();
    followers.push(average);
  }

  cout << days << endl;

  return 0;
}
