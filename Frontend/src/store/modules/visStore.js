import {
    dataService
} from "../../service";

const state = () => ({
    selFileName: '',
    fileData: undefined
});

const getters = {

}

const actions = {
    fetchData({
        state,
        commit
    }) {
        dataService.fetchData({fileName: state.selFileName}, resp => {
            commit('updateData', resp);
        })
    }
}

const mutations = {
    updateData(state, data) {
        state.data = data;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}