import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Random;


interface EventListener {
    void eventPerformed(EventObject e);
}

abstract class EventEmitterBlueprint {
    // instance, every instance has different object listeners registered

    private Hashtable<String, ArrayList<EventListener>> listeners = new Hashtable<>();
    public int x; // GUI position of emitter
    public int y; // GUI position of emitter

    private void initHashtable (String[] eventTypes) {
        for (int i=0;i<eventTypes.length; i++) {
            this.listeners.put(eventTypes[i], new ArrayList<>());
        }
    }

    public void registerEventListener(String type, EventListener listener) {
        ArrayList<EventListener> chosen = this.listeners.get(type);
        chosen.add(listener);
        System.out.println(this.listeners);
    }

    public void emitEvent(EventObject event) {

        if (this.listeners.containsKey(event.getName())) {
            for (EventListener listener: this.listeners.get(event.getName())) {
                listener.eventPerformed(event);
            }
        }
        else {
            System.out.println("This event type is not supported");
        }
    }

    EventEmitterBlueprint (String[] eventTypes, int x, int y) {
        this.initHashtable(eventTypes);
        this.x = x;
        this.y = y;
    }
}


class Button extends EventEmitterBlueprint {

    Button (String[] EventTypes, int x, int y) {
        super(EventTypes, x, y);
    }
}


class EventObject {

    private static String[] type = {"click", "hover", "socket", "close", "open"};
    private String name;

    private void setName() {
        this.name = type[genRandom()];
    }

    public String getName() {
        return this.name;
    }

    private int genRandom() {
        Random gen = new Random();
        int rndIndex = gen.nextInt(type.length);
        return rndIndex;
    }

    EventObject () { // on init, generate and set a random name
        setName();
    }
}


class EV implements EventListener {
    public void eventPerformed (EventObject event) {
        System.out.println("EV - it worked " + event.getName());
    }
}

class BM implements EventListener {
    public void eventPerformed (EventObject event) {
        System.out.println("BM - it worked " + event.getName());
    }
}

// Based on which event gets generated and what event type a listener is registered to, eventPerformed might be called()
// Event object creation simplified (not reading from standard input)
public class EventSystem {
    public static void main (String[] args) {
        Button btn1 = new Button(new String [] {"click", "hover", "socket"}, 10, 11); // event emitter
        Button btn2 = new Button(new String [] {"click", "hover", "socket", "close"}, 12, 15); // event emitter

        EV listener1 = new EV(); // event listener object
        BM listener2 = new BM();

        btn1.registerEventListener("click", listener1); // attach the listener to the emitter source
        btn2.registerEventListener("hover", listener2);

        btn1.emitEvent(new EventObject());
        btn2.emitEvent(new EventObject());
    }
}
