import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddRentalCar from '@/components/AddRentalCar'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AddRentalCar',
      component: AddRentalCar
    }
  ]
})
