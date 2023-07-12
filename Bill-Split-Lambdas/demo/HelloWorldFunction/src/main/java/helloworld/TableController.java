package helloworld;

import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.*;

@RestController
public class TableController {

    private Map<Long, List<MenuItem>> tableData = new HashMap<>();

    @PostMapping("/table")
    public void addTableData(@RequestBody TableItems data) {
        tableData.put(data.getId(), data.getItems());
    }

    @GetMapping("/table/{tableID}")
    public List<MenuItem> getTableData(@PathVariable long tableID) {
        return tableData.get(tableID);
    }
}
