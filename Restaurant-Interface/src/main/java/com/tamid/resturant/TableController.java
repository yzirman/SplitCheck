package com.tamid.resturant;

import java.util.*;
import java.util.concurrent.*;

import org.springframework.web.bind.annotation.*;

@RestController
public class TableController {

    private Map<Long, List<MenuItem>> tableData = new HashMap<>();
    int numThreads = Runtime.getRuntime().availableProcessors(); // get the number of threads available on the machine
    // ExecutorService is a threading framework
    private ExecutorService executorService = Executors.newFixedThreadPool(numThreads); // create a thread pool with however many threads are available on the machine

    /**
     * Adds data to the tableData map
     * @param data the data to add
     */
    @PostMapping("/table")
    public void addTableData(@RequestBody TableItems data) {
        // Callable is an object provided by the ExecutorService framework
        // Think of it as a task that gets submitted to the ExecutorService which then gets put into a queue to wait its turn
        // Runnable is another object provided by the framework
        Callable<Void> task = () -> {
            tableData.put(data.id(), data.items());
            return null;
        };
        executorService.submit(task);
    }

    /**
     * Gets the data from the tableData map
     * @param tableID the table ID to get data for
     * @return a list of MenuItems
     * @throws ExecutionException
     * @throws InterruptedException
     */
    @GetMapping("/table/{tableID}")
    public List<MenuItem> getTableData(@PathVariable long tableID) throws ExecutionException, InterruptedException {
        // Future is a Java interface
        // is used to retrieve the result of a computation that is being executed in a separate thread
        // allowing the main thread to continue executing while the result is being calculated
        Future<List<MenuItem>> future = executorService.submit(() -> tableData.get(tableID)); // submit a task (the tableData.get(tableID) is the "task") to the executor service to get the data for the table
        return future.get(); // get() blocks until the result is available
    }
}
