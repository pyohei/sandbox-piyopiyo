public class GamePlayer2 {
	public String playername;
	public GamePlayer2(String name) {
		playername = name;
	}
	public String toString() {
		return "[player:" + playername + "]";
	}
	public static void main (String[] args) {
		GamePlayer2[] player = new GamePlayer2[3];
		player[0] = new GamePlayer("Mad Hatter");
		player[1] = new GamePlayer("March Hare");
		player[2] = new GamePlayer("Alice");
		for (int i = 0; i < player.length; i++) {
			System.out.println(player[i]);
		}
	}
}