function showStatus(status) {
    switch (status) {
        case 'Escalation': return (`
      <div>
        <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-red-700"></div>
        <div>Escalation</div>
        </div>
      </div>
      `);
        case 'In progress': return (`
      <div>
       <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-orange-500"></div>
          <div>In progress</div>
        </div>
      </div>
      `);
        case 'Close': return (`
      <div>
        <div class="flex items-center space-x-2">
          <div class="h-5 w-5 rounded-full bg-green-500"></div>
          <div>Close</div>
          </div>
      </div>
      `);
    }
}

function showSeverity(severity) {
    switch (severity) {
        case 'Low': return (`
      <div>
        <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-green-700"></div>
        <div>Low</div>
        </div>
      </div>
      `);
        case 'Medium': return (`
      <div>
       <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-yellow-500"></div>
          <div>Medium</div>
        </div>
      </div>
      `);
        case 'High': return (`
      <div>
        <div class="flex items-center space-x-2">
          <div class="h-5 w-5 rounded-full bg-orange-500"></div>
          <div>High</div>
          </div>
      </div>
      `);
        case 'Critical': return (`
       <div>
        <div class="flex items-center space-x-2">
          <div class="h-5 w-5 rounded-full bg-red-600"></div>
          <div>Critical</div>
          </div>
      </div>
      `);
    }
}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;
    return [day, month, year].join('-');
}

function getData(id) {
    return $.ajax({
        url: '/ajax/getUserInfo/',
        type: 'GET', 
        data: {
            'id': id,
        }
    })
};

async function getUserInfo(id) {
    let result = null
    try {
        const res = await getData(id)
        result = JSON.parse(res)[0].fields.username
    } catch (err) {
        console.log(err);
    }
    return result
}

function getMainTableById(id){
  console.log('id = ',id)
}

function getMainTableResult() {
    $.ajax({
        url: '/ajax/getMaintable/',
        type: 'GET',
        success: async function (data) {
            const result = JSON.parse(data)
            for (var i = 0; i < result.length; i++) {
                const items = result[i].fields
                const jobPk = result[i].pk

                await getUserInfo(items.assign).then((value) => {
                    assignName = value
                })

                $("#jobData").append(`
                <tr>
                  <th>${items.ticket_id}</th>
                  <td>${formatDate(items.date)}</td>
                  <td>${items.search_name}</td>
                  <td>${showSeverity(items.severity)}</td>
                  <td>${showStatus(items.status)}</td>
                  <td>${assignName}</td>
                  <td>
                    <label for="my_modal_8" class="cursor-pointer">
                      <div class="flex items-center space-x-2">
                        <img class="w-5 h-5" src="https://cdn.discordapp.com/attachments/1095727305453752402/1141391343386644531/image.png">
                        <div class="text-xs" onclick="">View Result</div>
                      </div>
                    </label> 
                  </td>
                </tr>
                `)
           }
        }
    })
}

getMainTableResult()