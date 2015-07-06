using UnityEngine;
using System.Collections;
using System; //This allows the IComparable Interface

//This is the class you will be storing
//in the different collections. In order to use
//a collection's Sort() method, this class needs to
//implement the IComparable interface.
public class Site : IComparable<Site>
{
	
	public int height;
	public string name;
	
	public Site(int Height, string Name)
	{
		height = Height;
		name = Name;
	}
	
	//This method is required by the IComparable
	//interface. 
	public int CompareTo(Site other)
	{
		if(other == null)
		{
			return 1;
		}
		
		//Return the difference in height.
		return height - other.height;
	}
}