#include <iostream>
#include <stack>
#include <cmath>

using namespace std;

int main()
{
  long long followers, goal, average = 0, num, days = 0;
  stack<long long> followers_per_day;

  cin >> followers >> goal;

  while (followers_per_day.size() < 30)
  {
    cin >> num;
    followers_per_day.push(num);
    average += num;
  }

  cout << floor((goal - followers) / ceil(average / 30) + 1) << endl;

  return 0;
}
