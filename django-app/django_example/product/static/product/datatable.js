 $(document).ready(function() {
    $("#product_list").dataTable({
      processing: true,
      serverSide: false,
      ajax: {
        url: "/list",
        dataSrc: "",
      },
      columns: [
        { data: "pk" },
        { data: "fields.customer" },
        { data: "fields.name" },
        { data: "fields.price" },
        { data: "fields.description" },
      ],
    });
   });