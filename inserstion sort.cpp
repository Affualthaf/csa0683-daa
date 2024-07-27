#include<stdio.h>
int insertionsort(int num[],int n)
{
	int i,j,temp;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(num[j]<num[j+1])
			{
			temp=num[j];
			num[j]=num[j+1];
			num[j+1]=temp;
		}
		}
	}
}
int main()
{
	int num[]={65,76,98,34,1,4,77,54};
	int n=sizeof(num)/sizeof(num[0]);
	insertionsort(num,n);
	printf("after sorting:\n\n");
	for(int i=0;i<n;i++)
	printf("%d, ",num[i]);
	return 0;
}