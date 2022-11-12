// ============================ CORE CODE
// (scroll all the way down for the demo usage)

// utility for get/set/callback
const defineObservedProperty = (obj, prop, callback) =>
  Object.defineProperty(obj, prop, {
    get() { return obj[`_${prop}`] },
    set(val) {
      obj[`_${prop}`] = val
      callback(val)
    }
  })

// custom table element
class DynamicTable extends HTMLTableElement {
  
  constructor() {
    super()
    defineObservedProperty(
      this,
      'cells',
      this.dataChangedCallback.bind(this)
    )
    this.selectedClass = '_selected'
  }

  connectedCallback() {
    this.tBody = this.querySelector('tbody') || this.createTBody()
    this.rowTemplate = this.tBody.querySelector('tr') || document.createElement('tr')
    this.tBody.innerHTML = ''
    this.headers = [...this.querySelectorAll('th')]
    this.headers.forEach((header, idx) => {
      header.addEventListener('click', event => {
        const prevAsc = this.dataset.sortOrder === 'asc'
        const newCol = this.dataset.sortColumn !== idx.toString()
        if (newCol) this.dataset.sortColumn = idx
        this.dataset.sortOrder = prevAsc && !newCol ? 'desc' : 'asc'
      })
    })
  }
  
  static get observedAttributes() {
    return ['data-sort-column', 'data-sort-order']
  }

  attributeChangedCallback(name, oldVal, newVal) {
    if (this.tBody)
      this.sortRowsByColumn(
        this.dataset.sortOrder,
        this.dataset.sortColumn
      )
  }
  
  getEl(kind, context, idx) {
    const selector = kind === 'row' ? 'tr' : 'td'
    const capsKind = kind[0].toUpperCase() + kind.slice(1)
    const method = `add${capsKind}` // addRow|addCell
    const total = context.querySelectorAll(selector).length
    const missing = idx - total
    for (let i = 0; i <= missing; i++) this[method](context)
    return context.querySelectorAll(selector)[idx]
  }
  
  addRow() {
    const row = this.rowTemplate.cloneNode(true)
    this.getEl('cell', row, this.querySelectorAll('th').length-1)
    this.tBody.appendChild(row)
    return row
  }
  
  addCell(row) {
    const cell = document.createElement('td')
    row.appendChild(cell)
    return cell
  }
  
  dataChangedCallback() {
    this.cells.forEach(cell => {
      const [rowIdx, colIdx] = [cell.rowIdx, cell.columnIdx]
      const tr = this.getEl('row', this.tBody, rowIdx)
      const td = this.getEl('cell', tr, colIdx)
      td.textContent = cell.data
    })
    this.sortRowsByColumn(
      this.dataset.sortOrder,
      this.dataset.sortColumn
    )
  }
  
  toggleSelectedColumn(cellsInColumn, columnIdx) {
    this.headers.forEach(el => el.classList.remove(this.selectedClass))
    this.headers[columnIdx].classList.add(this.selectedClass)
    const allCells = [...this.tBody.querySelectorAll('td')]
    allCells.forEach(el => el.classList.remove(this.selectedClass))
    cellsInColumn.forEach(el => el.classList.add(this.selectedClass))
  }
  
  sortRowsByColumn(order, columnIdx) {
    const rows = [...this.tBody.rows]
    const cellsInColumn = rows.map(el => {
      return el.querySelectorAll('td')[columnIdx]
    })
    cellsInColumn.sort((el1, el2) => {
      const [txt1, txt2] = [el1.textContent, el2.textContent]
      const [num1, num2] = [+txt1 !== NaN ? +txt1 : 0, +txt1 !== NaN ? +txt2 : 0]
      const canSortNumbers = num1 && num2
      const asc = canSortNumbers ? num1 > num2 : txt1 > txt2
      const desc = canSortNumbers ? num1 < num2 : txt1 < txt2
      const ord = order === 'asc' ? asc : desc
      return ord ? 1 : -1
    })
    cellsInColumn.forEach(el => {
      const row = el.parentNode
      row.remove()
      this.tBody.appendChild(row)
    })
    this.toggleSelectedColumn(cellsInColumn, columnIdx)
  }

}

// Instantiates the object when the DOM is parsed
//   <table is="dynamic-table"></table>
customElements.define(
  'dynamic-table',
  DynamicTable,
  {extends: 'table'}
)




// ============================ DEMO CODE

const demoTable = document.querySelector('.table-js')

demoTable.cells = [
  {rowIdx: 0, columnIdx: 0, data: '12'},
  {rowIdx: 0, columnIdx: 1, data: '689'},
  
  {rowIdx: 1, columnIdx: 0, data: '792'},
  {rowIdx: 1, columnIdx: 1, data: '247'},
  
  {rowIdx: 2, columnIdx: 0, data: '869'},
  {rowIdx: 2, columnIdx: 1, data: '720'},
  
  {rowIdx: 3, columnIdx: 0, data: '214'},
  {rowIdx: 3, columnIdx: 1, data: '168'},
 
]
