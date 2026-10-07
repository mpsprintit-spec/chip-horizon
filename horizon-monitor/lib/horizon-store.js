export class HorizonStore {
  constructor(){this.snapshotValue=null;this.eventsValue=[];this.statusValue="disconnected";this.listeners=new Set;this.gapValue=null;this.revisionValue=0}
  get snapshot(){return this.snapshotValue}
  get events(){return this.eventsValue}
  get status(){return this.statusValue}
  get gap(){return this.gapValue}
  get revision(){return this.revisionValue}
  subscribe(listener){this.listeners.add(listener);return()=>this.listeners.delete(listener)}
  setStatus(status){this.statusValue=status;this.emit()}
  setSnapshot(snapshot){if(snapshot.type!=="brain.snapshot")throw new Error("invalid brain snapshot type");if(!Number.isFinite(snapshot.state_revision))throw new Error("invalid snapshot revision");this.snapshotValue=snapshot;this.revisionValue=snapshot.state_revision;this.gapValue=null;this.emit()}
  applyEvent(event){if(event.brain_identity&&this.snapshotValue&&event.brain_identity!==this.snapshotValue.brain_identity)throw new Error("telemetry brain identity mismatch");const revision=Number(event.state_revision);if(!Number.isFinite(revision))throw new Error("telemetry event has invalid revision");if(revision<=this.revision)return"duplicate";if(revision>this.revision+1){this.gapValue={expected:this.revision+1,received:revision};this.statusValue="resyncing";this.emit();return"gap"}this.eventsValue=[...this.eventsValue.slice(-499),event];this.revisionValue=revision;if(event.canonical_state_hash&&this.snapshotValue&&event.state_revision===this.snapshotValue.state_revision&&event.canonical_state_hash!==this.snapshotValue.canonical_state_hash){this.statusValue="error";this.emit();throw new Error("canonical state hash mismatch")}this.emit();return"applied"}
  replaceEvents(events){this.eventsValue=events.slice(-500);this.emit()}
  clearForReconnect(){this.statusValue="connecting";this.emit()}
  emit(){for(const listener of this.listeners)listener()}
}
