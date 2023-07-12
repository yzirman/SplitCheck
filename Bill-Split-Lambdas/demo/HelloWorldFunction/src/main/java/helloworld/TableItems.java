package helloworld;

import java.util.List;

public class TableItems {
    private final long id;
    private final List<MenuItem> items;

    public TableItems(long id, List<MenuItem> items) {
        this.id = id;
        this.items = items;
    }

    public long getId() {
        return id;
    }

    public List<MenuItem> getItems() {
        return items;
    }
}
