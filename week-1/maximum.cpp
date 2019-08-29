#include<iostream>
using namespace std;

int findMax(int a[], int n){
    int m = a[0];
    for(int i=1; i<n; i++)
        if(a[i] > m)
            m = a[i];
    return m;
}

int main(){
    int arr[100], n, m;
    cout<<"Enter the number of elements in the array ";
    cin>>n;
    cout<<"Enter the elements of the array ";
    for(int i=0; i<n; i++)
        cin>>arr[i];
    m = findMax(arr,n);
    cout<<"The maximum of the numbers is "<<m;
    return 0;
}
