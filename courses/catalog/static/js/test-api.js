(function () {
    function goBack() {
        window.history.back();
    }

    function getData() {
        return fetch('/catalog/');
    }

    function rowTemplate(idx, fields) {
        return `
            <tr>
                <th scope="row">${idx}</th>
                <td>${fields.title}</td>
                <td>${fields.number_of_lectures}</td>
                <td>${fields.start_date}</td>
                <td>${fields.end_date}</td>
            </tr>
        `
    }

    function renderTable(data){
        const $tableBodyEl = $('.course-table tbody')

        data.forEach(((model, idx) => {
            $tableBodyEl.append(rowTemplate(idx, model.fields))
        }))
    }
    async function render() {

        const data = await getData()
            .then(response => response.json());
        console.log('Fetched data:', data)
        renderTable(data);
    }

    console.log('test-api.module')
    // globals
    return Object.assign(window, {goBack, render})
})()