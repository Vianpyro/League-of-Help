function search_champion() {
    // Declare variables
    let input, filter, parent, figure, a, i, txtValue;
    input = document.getElementById('search-champion');
    filter = input.value.toUpperCase();
    parent = document.getElementById("champions");
    figure = parent.getElementsByTagName('figure');

    // Loop through all figurest items, and hide those who don't match the search query
    for (i = 0; i < figure.length; i++) {
        a = figure[i].getElementsByTagName("a")[0];

        txtValue = a.textContent || a.innerText;

        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            figure[i].style.display = "";
        }
        else {
            figure[i].style.display = "none";
        }
    }
}