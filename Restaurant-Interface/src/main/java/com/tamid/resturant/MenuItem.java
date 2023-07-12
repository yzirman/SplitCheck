package com.tamid.resturant;

public class MenuItem implements Comparable<MenuItem> {
    private String name;
    private double price;

    public MenuItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public int compareTo(MenuItem o) {
        if (this.name.equals(o.name) && this.price == o.price) {
            return 0;
        }
        return 1;
    }
}
