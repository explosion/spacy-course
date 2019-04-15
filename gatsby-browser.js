import Juniper from './src/components/juniper'

export const onInitialClientRender = () => {
    // Importing Juniper in the component currently causes various problems
    // because of the global window reference in its dependencies. So this
    // is kinda hacky at the moment.
    window.Juniper = Juniper
}
