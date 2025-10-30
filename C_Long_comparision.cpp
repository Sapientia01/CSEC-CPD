// #include<iostream>
#include <iostream>

using namespace std;


int main() {
    int t;
    
    cin >> t;
    for (int i ; i < t; i++) {
        int x1,x2,p1,p2,num1,num2;
        cin >> x1>>p1>>x2>>p2;

         num1 = x1 * (10**p1)
         num2 = x2 * (10**p2)

        if (num1 > num2)
            {cout<< ">"<< endl;}
        else if (num1 < num2)  
            { cout<< "<"<< endl;}
        else:
            {cout<< "="<< endl;}

    }

    return 0
}
