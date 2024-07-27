#include<stdio.h>
int binarysearch(int arr[],int x,int low,int high)
{
	while(low<=high)
	{
	int mid=(low+(high))/2;
	if(arr[mid]==x)
	return mid;
	if(x>arr[mid])
	low=mid+1;
	else
	high=mid-1;
}
return -1;
}
int main()
{
	int arr[]={2,4,5,8,7,9};
	int n=sizeof(arr)/sizeof(arr[0]);
	int x=10;
	int result=binarysearch(arr,x,0,n-1);
	if(result==-1)
	printf("element not found");
	else
	printf("element found at index %d",result+1);
	return 0;
}