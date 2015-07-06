class Tuple
{
	int x;
	int y;
	
	public Tuple(int x, int y)
	{
		this.x = x;
		this.y = y;
	}
	
	public int X { get { return x; } }
	public int Y { get { return y; } }
	
	public override int GetHashCode()
	{
		return x.GetHashCode() ^ y.GetHashCode() ;
	}
	
	public override bool Equals(object obj)
	{
		if (obj == null || GetType() != obj.GetType())
		{
			return false;
		}
		return Equals((Tuple)obj);
	}
	
	public bool Equals(Tuple other)
	{
		return other.x.Equals(x) && other.y.Equals(y);
	}
}