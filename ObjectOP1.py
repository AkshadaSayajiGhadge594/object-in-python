##############################################################
##  OBJECT ORIENTED APPLICATION in Python
#############################################################
	
class Bank:

	ROI = 10.3;

	def __init__(self,custname,value):
		self.name=custname;
		self.amount=value;

	def Deposite(self,value):
		self.amount = self.amount + value;
	
	def Withdraw(self,value):
		self.amount = self.amount - value;
	
	@classmethod
	def DisplayROI(cls):
		print(cls.ROI);
	
	@staticmethod
	def BankInfo():
		print("It is nationlised bank of India");
		print("Location is Satara"); 


def main():
	obj1 = Bank("Akshay",20000);
	print(obj1.name);
	print(obj1.amount);
	
	obj2 = Bank("Nikhil",30000);
	print(obj2.name);
	print(obj2.amount);
	
	obj1.Deposite(500);
	obj2.Deposite(500);
	
	print(obj1.amount);
	print(obj2.amount);

	obj1.Withdraw(200);
	obj2.Withdraw(300);

	print(obj1.amount);
	print(obj2.amount);

	Bank.DisplayROI();
	Bank.BankInfo();

	



if __name__ =="__main__":
	main();
