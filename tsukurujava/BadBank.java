// List16-3

public class BadBank {
	//credit balance
	private int value = 0;
	// deposit
	public void addMoney (int money) {
		// reserve present balance
		int currentValue = value;
		// curcumstance
		System.out.println (Thread.currentThread() + "が addMoney に入りました。 ");
		// change present balance
		value += money;
		//check the contradiction
		if ( currentValue + money != value) {
			System.out.println (Thread.currentThread() + " で矛盾が生じています ");
			System.exit(-1);
		}
		//represent curcumstance
		System.out.println(Thread.currentThread() + "が addMoney から出ました。");
	}
}
