# include <stdio.h>
void read (int a[10][10],int n, int m)
{
    int i, j;
    for(i=0; i<n; i++)
    {
        for(j=0; j<m; j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
}
void display(int a[10][10],int n, int m)
{
    int i, j;
    for(i=0; i<n; i++)
    {