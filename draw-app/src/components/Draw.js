import React from 'react'
import {SketchField, Tools} from 'react-sketch'

const Draw = () => {
    return (
        <React.Fragment>
            <SketchField
                width='800px'
                height='800px'
                tool={Tools.Pencil}
                backgroundColor='black'
                lineColor='white'
                imageFormat='jpg'
                lineWidth={60}
            />
        </React.Fragment>
    )
}

export default Draw