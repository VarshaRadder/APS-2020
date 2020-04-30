#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<stack>			 
using namespace std;

typedef struct Node
{
	int data;
	struct Node *link;
}node;

node *head = NULL;		

/* Driver functions */
void Reverse();
void insert(int data, int position);
void print();

/* Main method */
int main()
{
	insert(0,1);	
insert(1,2);
insert(2,3);
insert(3,4);

	print();		
	Reverse();

	print();		
	return 0;
}


void insert(int data, int position)
{
	node *temp = (node*)malloc(sizeof(node));
	temp->data = data;
	temp->link = NULL;

	if(position==1)
	{
		temp->link = head;
		head = temp;
		return ;
	}

	node *traverse = head;

	for(int i=0; i<position-2; i++)
	{
		traverse = traverse->link;
	}

	temp->link = traverse->link;
	traverse->link = temp;

}

void print()
{
	node *p = head;
	while(p)
	{
		printf(" %d",p->data);
		p = p->link;
	}
	printf(" \n\n ");
}


void Reverse()
{
	stack<node*> Stack;
	node *traverse = head;

	
	while(traverse!=NULL)
	{
		Stack.push(traverse);
		traverse = traverse->link;
	}

	
	node *temp = Stack.top();
	head = temp;
	Stack.pop();
	while(!Stack.empty())
	{

		temp->link = Stack.top();
		Stack.pop();
		temp = temp->link;
	}
	temp->link = NULL;				
}
