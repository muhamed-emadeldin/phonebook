$(document).ready(function() {
    var devDown = document.getElementById('devDown')
    var devWarn = document.getElementById('devWarning')
    var devType = document.getElementById('devTypes')
    var snippet = document.getElementById('snippet')
    var writeInTbl = document.getElementById('write-table')
    var setWidthModal = document.getElementById('set-width-modal')


    devDown.setAttribute('data-bs-toggle', 'modal')
    devDown.setAttribute('data-bs-target', '#exampleModal')
    devDown.onclick = function() {
        writeInTbl.innerHTML = ''

        snippet.style.display = 'block';
        snippet.setAttribute('class', 'row-fluid text-center show')

        var tDynHeader = document.getElementById('table-dynamic-header')
        tDynHeader.innerHTML = ''

        setWidthModal.style.maxWidth = '500px'



        var devDownArray = ["region", "Device down"]
        var modalHeader = document.getElementById('exampleModalLabel')
        modalHeader.setAttribute("class", "text-uppercase text-danger")
        modalHeader.innerHTML = "Device Down"



        $.ajax({
            type: 'POST',
            url: window.location.href,
            headers: {
                'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
            },
            data: { "which_link": 'device-down' },
            success: function(data) {
                snippet.style.display = 'none';
                snippet.setAttribute('class', 'row-fluid text-center fade')
                count = 0

                for (let index = 0; index < devDownArray.length; index++) {
                    elem = devDownArray[index]
                    var thDynTable = document.createElement('th')
                    thDynTable.setAttribute('id', 'thDynTable' + index)
                    thDynTable.setAttribute('class', 'text-uppercase text-Secondary text-xxs font-weight-bolder opacity-7 ps-2')
                    thDynTable.innerHTML = elem
                    document.querySelector('#table-dynamic-header').appendChild(thDynTable);
                }

                for (elm in data) {
                    var trTag = document.createElement('tr');
                    var tdKTag = document.createElement('td');
                    var tpKTag = document.createElement('p');
                    var tdVTag = document.createElement('td');
                    var tpVTag = document.createElement('p');

                    trTag.setAttribute('id', 'trTag' + count)
                    trTag.setAttribute('class', 'justify-content-md-center')
                    document.querySelector('#write-table').appendChild(trTag);

                    tdKTag.setAttribute('id', 'tdKTag' + count)
                    tdKTag.setAttribute('class', 'align-middle text-center')
                    document.querySelector('#trTag' + count).appendChild(tdKTag);

                    tpKTag.setAttribute('id', 'tpKTag' + count)
                    tpKTag.setAttribute('class', 'text-xs font-weight-bold mb-0')
                    tpKTag.innerHTML = elm
                    document.querySelector('#tdKTag' + count).appendChild(tpKTag);

                    tdVTag.setAttribute('id', 'tdVTag' + count)
                    tdVTag.setAttribute('class', 'align-middle text-center')
                    document.querySelector('#trTag' + count).appendChild(tdVTag);

                    tpVTag.setAttribute('id', 'tpVTag' + count)
                    tpVTag.setAttribute('class', 'text-xs font-weight-bold mb-0')
                    tpVTag.innerHTML = data[elm]
                    document.querySelector('#tdVTag' + count).appendChild(tpVTag);

                    count++;

                }
            }

        })
    }

    devWarn.setAttribute('data-bs-toggle', 'modal')
    devWarn.setAttribute('data-bs-target', '#exampleModal')
    devWarn.onclick = function() {
        writeInTbl.innerHTML = ''

        snippet.style.display = 'block';
        snippet.setAttribute('class', 'row-fluid text-center show')

        var tDynHeader = document.getElementById('table-dynamic-header')
        tDynHeader.innerHTML = ''

        var modalHeader = document.getElementById('exampleModalLabel')

        setWidthModal.style.maxWidth = '90vw'

        modalHeader.setAttribute("class", "text-uppercase text-warning")
        modalHeader.innerHTML = "HIGHLY UTILIZED LINK"

        $.ajax({
            type: 'POST',
            url: window.location.href,
            headers: {
                'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
            },
            data: { "which_link": 'device-warning' },
            success: function(data) {
                snippet.style.display = 'none';
                snippet.setAttribute('class', 'row-fluid text-center fade')
                count = 0
                i = 0

                var regionKeys = Object.keys(Object.values(data)[0])

                for (let index = 0; index < regionKeys.length; index++) {
                    elem = regionKeys[index]
                    var thDynTable = document.createElement('th')
                    thDynTable.setAttribute('id', 'thDynTable' + index)
                    thDynTable.setAttribute('class', 'text-uppercase text-Secondary text-xxs font-weight-bolder opacity-7 ps-2')
                    thDynTable.innerHTML = elem
                    document.querySelector('#table-dynamic-header').appendChild(thDynTable);
                }

                for (keys in data) {
                    var trDynTable = document.createElement('tr')
                    trDynTable.setAttribute('id', 'trDynTable' + count)
                    document.querySelector('#write-table').appendChild(trDynTable);
                    for (row in data[keys]) {
                        var tdDynTable = document.createElement('td')
                        tdDynTable.setAttribute('id', 'tdDynTable' + i)
                        tdDynTable.setAttribute('class', 'align-middle text-center')
                        document.querySelector('#trDynTable' + count).appendChild(tdDynTable);

                        for (let index = 0; index < data[keys][row].length; index++) {
                            var element = data[keys][row][index];
                            if (typeof(element) == 'number') {
                                element = Math.trunc(element)
                            }
                            var tpDynTable = document.createElement('p')
                            tpDynTable.setAttribute('id', 'tpDynTable' + index)
                            tpDynTable.setAttribute('class', 'text-secondary text-xs font-weight-bold')
                            tpDynTable.innerHTML = element
                            document.querySelector('#tdDynTable' + i).appendChild(tpDynTable);



                        }
                        i++;
                    }
                    count++;

                }


            }

        })
    }


    devType.setAttribute('data-bs-toggle', 'modal')
    devType.setAttribute('data-bs-target', '#exampleModal')
    devType.onclick = function() {
        writeInTbl.innerHTML = ''

        snippet.style.display = 'block';
        snippet.setAttribute('class', 'row-fluid text-center show')

        var tDynHeader = document.getElementById('table-dynamic-header')
        tDynHeader.innerHTML = ''

        var modalHeader = document.getElementById('exampleModalLabel')

        setWidthModal.style.maxWidth = '500px'

        modalHeader.setAttribute("class", "text-uppercase text-info")
        modalHeader.innerHTML = "DEVICES PER TYPE"

        var devTypeArray = ["Type", "Count"]

        $.ajax({
            type: 'POST',
            url: window.location.href,
            headers: {
                'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
            },
            data: { "which_link": 'device-types' },
            success: function(data) {
                snippet.style.display = 'none';
                snippet.setAttribute('class', 'row-fluid text-center fade')
                count = 0

                for (let index = 0; index < devTypeArray.length; index++) {
                    elem = devTypeArray[index]
                    var thDynTable = document.createElement('th')
                    thDynTable.setAttribute('id', 'thDynTable' + index)
                    thDynTable.setAttribute('class', 'text-uppercase text-Secondary text-xxs font-weight-bolder opacity-7 ps-2')
                    thDynTable.innerHTML = elem
                    document.querySelector('#table-dynamic-header').appendChild(thDynTable);
                }

                for (elm in data) {
                    var trTag = document.createElement('tr');
                    var tdKTag = document.createElement('td');
                    var tpKTag = document.createElement('p');
                    var tdVTag = document.createElement('td');
                    var tpVTag = document.createElement('p');

                    trTag.setAttribute('id', 'trTag' + count)
                    trTag.setAttribute('class', 'justify-content-md-center')
                    document.querySelector('#write-table').appendChild(trTag);

                    tdKTag.setAttribute('id', 'tdKTag' + count)
                    tdKTag.setAttribute('class', 'align-middle text-center')
                    document.querySelector('#trTag' + count).appendChild(tdKTag);

                    tpKTag.setAttribute('id', 'tpKTag' + count)
                    tpKTag.setAttribute('class', 'text-xs font-weight-bold mb-0')
                    tpKTag.innerHTML = elm
                    document.querySelector('#tdKTag' + count).appendChild(tpKTag);

                    tdVTag.setAttribute('id', 'tdVTag' + count)
                    tdVTag.setAttribute('class', 'align-middle text-center')
                    document.querySelector('#trTag' + count).appendChild(tdVTag);

                    tpVTag.setAttribute('id', 'tpVTag' + count)
                    tpVTag.setAttribute('class', 'text-xs font-weight-bold mb-0')
                    tpVTag.innerHTML = data[elm]
                    document.querySelector('#tdVTag' + count).appendChild(tpVTag);

                    count++;

                }
            }

        })
    }

})