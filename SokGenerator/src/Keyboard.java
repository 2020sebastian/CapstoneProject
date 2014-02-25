
public class Keyboard {
	
	//class that represents a virtual keyboard
	
	public final String typeOfKeyboard = "";
	public final Key a = new Key();

private class Key{
	public String name = ""; //name of key
	
		// center coordinate
		public int centerX;
		public int centerY;
		
		//upper left corner
		public int upperLeftX;
		public int upperLeftY;
		
		//upper Right corner
		public int upperRightX;
		public int upperRightY;

		//lower left corner
		public int lowerLeftX;
		public int lowerLeftY;
		
		//lower right corner
		public int lowerRightX; 
		public int lowerRightY;
	
	public Key(String name, int centerX, int centerY, int upperLeftX, int upperLeftY, int upperRightX, int upperRightY,
			   int lowerLeftX, int lowerLeftY, int lowerRightX, int lowerRightY){
		this.name = name;
		this.centerX = centerX;
		this.centerY = centerY;
		this.upperLeftX = upperLeftX;
		this.upperLeftY = upperLeftY;
		this.upperRightX = upperRightX;
		this.upperRightY = upperRightY;
		this.lowerLeftX = lowerLeftX;
		this.lowerLeftY = lowerLeftY;
		this.lowerRightX = lowerRightX;
		this.lowerRightY = lowerRightY;
	}

	public Key() {
		this.name = "";
		this.centerX = 0;
		this.centerY = 0;
		this.upperLeftX = 0;
		this.upperLeftY = 0;
		this.upperRightX = 0;
		this.upperRightY = 0;
		this.lowerLeftX = 0;
		this.lowerLeftY = 0;
		this.lowerRightX = 0;
		this.lowerRightY = 0;
	}
	
}
}
