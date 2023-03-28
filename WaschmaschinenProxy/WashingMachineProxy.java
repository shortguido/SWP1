public class WashingMachineProxy implements WashingMachine {
    private WashingMachine currentMachine;

    public WashingMachineProxy(WashingMachine currentMachine) {
        this.currentMachine = currentMachine;
    }

    public void switchTo(WashingMachine newMachine) {
        this.currentMachine = newMachine;
    }

    @Override
    public void wash() {
        this.currentMachine.wash();
    }


public static void main(String[] args) {
    WashingMachine fourKgMachine = new FourKgWashingMachine();
    WashingMachine sevenKgMachine = new SevenKgWashingMachine();

    WashingMachineProxy proxy = new WashingMachineProxy(fourKgMachine);
    proxy.wash(); // Washing clothes in 4kg washing machine

    proxy.switchTo(sevenKgMachine);
    proxy.wash(); // Washing clothes in 7kg washing machine
}
}