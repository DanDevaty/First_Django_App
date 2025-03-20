$(document).ready(function() {
    $.ajaxSetup({
        headers: { 'X-CSRFToken': '{{ csrf_token }}' }
    });

    // Označit úkol jako dokončený
    $(".mark-completed").click(function() {
        var taskId = $(this).data('task-id');
        var button = $(this);
        $.post("{% url 'mark_completed_ajax' %}", { task_id: taskId }, function(response) {
            if (response.status == "success") {
                $("#todo-" + taskId + " .badge").removeClass('bg-secondary').addClass('bg-success').text('Hotovo');
                button.prop("disabled", true);
            } else {
                console.log('Error:', response.message);
            }
        });
    });

    // Smazat úkol
    $(document).on("click", ".delete-todo", function() {
        var taskId = $(this).data('task-id');
        $.ajax({
            url: "{% url 'delete_todo_ajax' %}",
            type: "POST",
            data: { task_id: taskId },
            success: function(response) {
                if (response.status === "success") {
                    $("#todo-" + taskId).fadeOut(300, function() { $(this).remove(); });
                } else {
                    console.log("Error:", response.message);
                }
            },
            error: function(xhr) {
                console.log("Došlo k chybě:", xhr.responseText);
            }
        });
    });
});
