import java.time.LocalTime;



public class Meet {
    public static final LocalTime EARLIEST_POSSIBLE_HOUR = LocalTime.of(8, 0);
    private String description;
    private LocalTime startTime;
    private LocalTime endTime;
    private String priority;

    public Meet(String description, LocalTime startTime, LocalTime endTime, String priority) {
        this.description = description;
        this.startTime = startTime;
        this.endTime = endTime;
        this.priority = priority;
    }

    public String getPriority() {
        return priority;
    }

    public LocalTime getStartTime() {
        return startTime;
    }

    public LocalTime getEndTime() { return endTime; }

    @Override
    public String toString() {
        return String.format("%s - %s\nPriority: %s\nDescription: %s\n", startTime, endTime, priority, description);
    }
}
