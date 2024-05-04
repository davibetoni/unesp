#include <iostream>
#include <queue>
#include <stack>
#include <cctype>

using namespace std;

bool isOperator(char ch)
{
  return (ch == '^' || ch == '*' || ch == '/' || ch == '+' || ch == '-' ||
          ch == '>' || ch == '<' || ch == '=' || ch == '#' || ch == '.' || ch == '|');
}

int getPriority(char op)
{
  switch (op)
  {
  case '^':
    return 6;
  case '*':
  case '/':
    return 5;
  case '+':
  case '-':
    return 4;
  case '>':
  case '<':
  case '=':
  case '#':
    return 3;
  case '.':
    return 2;
  case '|':
    return 1;
  default:
    return -1;
  }
}

void evaluateExpression(const string &expression, queue<string> &puts)
{
  string output;
  stack<char> operators;

  char last_char = '#';
  for (char ch : expression)
  {
    if (isdigit(ch) || isalpha(ch))
    {
      if (isdigit(last_char) || isalpha(last_char))
      {
        puts.push("Syntax Error!");
        return;
      }
      string operand(1, ch);
      output += operand;
    }
    else if (ch == '(')
    {
      if (last_char != '#' && (isdigit(last_char) || isalpha(last_char)))
      {
        puts.push("Syntax Error!");
        return;
      }
      operators.push(ch);
    }
    else if (ch == ')')
    {
      if (last_char != ')' && (!isdigit(last_char) && !isalpha(last_char)))
      {
        puts.push("Syntax Error!");
        return;
      }
      while (!operators.empty() && operators.top() != '(')
      {
        string op(1, operators.top());
        output += op;
        operators.pop();
      }
      if (!operators.empty() && operators.top() == '(')
      {
        operators.pop();
      }
      else
      {
        puts.push("Syntax Error!");
        return;
      }
    }
    else if (isOperator(ch))
    {
      if (isOperator(last_char))
      {
        puts.push("Syntax Error!");
        return;
      }

      if (last_char == '#' || last_char == '(')
      {
        if (ch == '-')
        {
          string operand(1, ch);
          output += operand;
        }
        else
        {
          puts.push("Syntax Error!");
          return;
        }
      }
      else
      {
        while (!operators.empty() && getPriority(ch) <= getPriority(operators.top()))
        {
          string op(1, operators.top());
          output += op;
          operators.pop();
        }
        operators.push(ch);
      }
    }
    else
    {
      puts.push("Lexical Error!");
      return;
    }
    last_char = ch;
  }

  while (!operators.empty())
  {
    if (operators.top() == '(' || operators.top() == ')')
    {
      puts.push("Syntax Error!");
      return;
    }
    string op(1, operators.top());
    output += op;
    operators.pop();
  }

  puts.push(output);
}

int main()
{
  string expression;
  queue<string> puts;

  while (cin >> expression)
  {
    evaluateExpression(expression, puts);
  }

  while (!puts.empty())
  {
    cout << puts.front() << endl;
    puts.pop();
  }

  return 0;
}
