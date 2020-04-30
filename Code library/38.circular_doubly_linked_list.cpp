#include<iostream>
using namespace std;

struct Node
{
	int val;
	Node *prev;
	Node *next;
};

Node *head;

void insert_rear(int value)
{

	
	Node *newNode = new Node;

	
	newNode->val = value;

	if(head == NULL)
	{
		
		newNode->prev = newNode;

		
		head = newNode;

		
		newNode->next=head;

	}
	else
	{
		
		Node* temp = head->prev;

		
        head->prev = newNode;

        
        newNode->prev = temp;

        
        newNode->next = head;

       
        temp->next = newNode;


	}
}

void remove(int x)
{
	if(head == NULL)
	{
		cout<<"\nList is Empty.\n"<<endl;

	}
	else
	{
		if(head->val == x)
		{
			//if the head value is equal to element to be deleted
			if(head->next == head)
			{
				//if there is only 1 element
				head=NULL;
			}
			else
			{
				Node* temp = head->prev;
				head = head->next;
				head->prev = temp;
				temp->next = head;
			}
			return;
		}
		Node* temp = head->next;
		while(temp != head && temp->val != x)
		{
			temp = temp->next;
		}
		if(temp == head)
		{
			cout<<"Value not found in list\n"<<endl;
		}
		else
		{
			temp->prev->next = temp->next;
			temp->next->prev = temp->prev;
		}
	}
}

void search(int x)
{
	Node *temp = head;
	int found = 0;

	do
	{
		if(temp->val == x)
		{
			cout<<"\nFound";
			found = 1;
			break;
		}
		temp = temp->next;
	}while(temp != head);

	if(found == 0)
	{
		cout<<"\nNot Found";
	}
}

void display()
{
	Node *temp = head;

	do
	{
		cout<< temp->val<<"\t";
		temp = temp->next;
	}while(temp != head);

}


int main()
{
	int choice, x;
	do
	{
		cout<<"\n1. Insert";
		cout<<"\n2. Delete";
		cout<<"\n3. Search";
		cout<<"\n4. Display";
		cout<<"\n5. Exit";
		cout<<"\n\nEnter you choice : ";
		cin>>choice;
		switch (choice)
		{
			case 1 : 	cout<<"\nEnter the element to be inserted at rear : ";
					 	cin>>x;;
					 	insert_rear(x);
					 	break;

			case 2 : 	cout<<"\nEnter the element to be removed : ";
						cin>>x;
						remove(x);
						break;

			case 3 : 	cout<<"\nEnter the element to be searched : ";
						cin>>x;
						search(x);
						break;

			case 4 : 	display();
						break;

		}
	}
	while(choice != 5);

	return 0;
}
