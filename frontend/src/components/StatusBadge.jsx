export function StatusBadge({status}){return <span className='rounded-full bg-shms-info/10 px-2 py-1 text-xs font-semibold text-shms-info'>{String(status||'unknown').replaceAll('_',' ')}</span>}
