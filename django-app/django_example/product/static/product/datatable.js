 $(document).ready(function() {
    $("#product_list").dataTable({
      processing: true,
      serverSide: false,
      ajax: {
        url: "/list",
        dataSrc: "",
      },
      columns: [
        { data: "id" },
        { data: "customer_name" },
        { data: "name" },
        { data: "price" },
        { data: "description" },
      ],
    });
   });