import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';
declare var jQuery: any;
import DataTable from 'jquery.datatables';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  // 2 准备数据
  homeTitle = 'HomeTitle';

  myString = 'I like pizza!';

  person = {
    name :  'Henry',
    color :  'yellow'
  };

  sites = ['菜鸟教程', 'Google', 'Taobao', 'Facebook'];

  mySite = this.sites[0];

  customerList = [
    {CID: '123', cName: 'Jacky'},
    {CID: '234', cName: 'Alan'}
  ];

  public config: any = {
    paging: true,
    sorting: {columns: this.columns},
    filtering: {filterString: ''},
    className: ['table-bordered']
  }
    columns = [
      {name: 'id',
        title: 'id'},
      {name: 'title',
        title: 'title'}
    ];

  dtOptions = {
    pagingType: 'full_numbers',
    order: [[2, 'desc']],
    destroy: true,  //解决Cannot reinitialise DataTable
    lengthChange: false,
    info: false,
    language: {
      'paginate': {
        'first':      '首页',
        'last':       '末页',
        'next':       '下一页',
        'previous':   '上一页'
      },
      'zeroRecords':    '没有查询到匹配的数据',
      'search': '搜索',
      'emptyTable':     '当前文件夹为空',
      // 'info':           '共 _TOTAL_ ',
    },
    columns: [
      { orderable: false },
      { orderable: false },
      null,
      { orderable: false },
      { orderable: false },
    ]
  };

  constructor() {
    /*$(document).ready(function () {
        $('#example').DataTable({
            bSort: false,
            "scrollY": "200px",
            "info": true
          }
        );


    });*/

  }

  ngOnInit() {
  }




}
